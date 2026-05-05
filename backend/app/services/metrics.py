from datetime import datetime

def calculate_mttr(start, end):
    return (end - start).total_seconds()
