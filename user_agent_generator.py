from bs4 import BeautifulSoup
import httpx
import ssl
import truststore

ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

def get_user_agents():
    url = "https://www.useragentlist.net/"
    request = httpx.get(url, verify=ssl_context)
    user_agents = []
    soup = BeautifulSoup(request.text, "html.parser")
    for user_agent in soup.select("pre.wp-block-code"):
        user_agents.append(user_agent.text.strip())
    return user_agents
