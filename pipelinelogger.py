import logging

logging.basicConfig(filename="pipeline.log", level=logging.INFO)

def log_message(message):
    logging.info(message)
    print(message)

if __name__ == "__main__":
    log_message("Pipeline execution started.")
