import logging
import sys

def setup_logger():
    # Only configure if no handlers are present to prevent duplicate logs
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )
