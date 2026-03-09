from src.utils.financial import preload_data
from src.ui.ui import build_root
from src.utils.file import write_tickers_info
from src.ui.cli_entry import CLIEntry
from src.utils.io import fetch_history

if __name__ == "__main__":
    #write_tickers_info(5000)
    #preload_data(n=30)

    root, input_frame = build_root()
    entry = CLIEntry(root, input_frame)
    root.mainloop()

###sum 4 q yoy + sec
