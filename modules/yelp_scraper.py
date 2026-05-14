import urllib.robotparser
import logging

def can_scrape(url: str) -> bool:
    try:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url("https://www.yelp.com.au/robots.txt")
        rp.read()

        allowed= rp.can_fetch("*", url)
        if not allowed:
            logging.warning(f"robots.txt disallows: {url}")

        return allowed
    
    except Exception as e:
        logging.error(f"Error while checking robots.txt: {e}")
        return True
