import diskcache as dc
from pathlib import Path
from src.utils.worker_registry import WorkerRegistry

#UI
registry = WorkerRegistry()
cache_path = Path.cwd() / "data" / "cache_dir"
cache = dc.Cache(cache_path, size_limit=1e9) #1GB
expiration_s = None
LIVE=False
SIZE = 10
sources = ["'Benzinga'", "'Reuters'", "'Yahoo Finance'", "'Seeking Alpha'", "'Quiver Quantitative'"]#"'TipRanks'", "'MarketWatch'", "'PR Newswire'", "'Business Wire'", "'GlobeNewswire'"]

#Model
SHIFT = 1

if __name__=="__main__":
    print("[DEBUG] registry is:", registry)
    print(source_filter)
