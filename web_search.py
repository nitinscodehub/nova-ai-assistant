"""Web search functionality using DuckDuckGo."""
from typing import List, Dict, Optional
from error_handler import ErrorHandler
from colorama import Fore, Style, init

init(autoreset=True)

class WebSearch:
    """Handles web search operations."""
    
    def __init__(self, config):
        self.config = config
        self.mode = config.get("mode", "offline")
        self._setup()
    
    def _setup(self):
        """Setup web search module."""
        if self.mode == "online":
            try:
                ErrorHandler.ensure_package("duckduckgo-search")
                print("✓ Web search ready (DuckDuckGo)")
            except Exception as e:
                print(f"⚠ Web search setup failed: {e}")
    
    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Search the web for a query."""
        if self.mode == "offline":
            return [{"title": "Web search requires online mode", "snippet": "Please enable online mode in settings.json", "url": ""}]
        
        try:
            from duckduckgo_search import DDGS
            
            print(f"{Fore.CYAN}Searching the web for: {query}{Style.RESET_ALL}")
            results = []
            
            with DDGS() as ddgs:
                for result in ddgs.text(query, max_results=max_results):
                    results.append({
                        "title": result.get("title", ""),
                        "snippet": result.get("body", ""),
                        "url": result.get("href", "")
                    })
            
            return results
        except Exception as e:
            print(f"{Fore.RED}Web search error: {e}{Style.RESET_ALL}")
            return [{"title": "Search failed", "snippet": str(e), "url": ""}]
    
    def format_results(self, results: List[Dict[str, str]]) -> str:
        """Format search results for display."""
        if not results:
            return "No results found."
        
        formatted = f"{Fore.GREEN}Top {len(results)} results:{Style.RESET_ALL}\n\n"
        for i, result in enumerate(results, 1):
            formatted += f"{Fore.YELLOW}{i}. {result.get('title', 'No title')}{Style.RESET_ALL}\n"
            formatted += f"   {result.get('snippet', 'No snippet')[:100]}...\n"
            formatted += f"   {Fore.CYAN}{result.get('url', 'No URL')}{Style.RESET_ALL}\n\n"
        return formatted
    
    def get_summary(self, query: str) -> str:
        """Get a summary of search results."""
        results = self.search(query, max_results=3)
        if not results or "requires online" in results[0].get("title", ""):
            return "Web search is not available in offline mode. Please enable online mode."
        
        summary = f"Here's what I found about {query}:\n"
        for result in results[:2]:
            summary += f"- {result.get('snippet', '')[:150]}...\n"
        return summary

