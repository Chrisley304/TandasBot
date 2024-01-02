from notion_client import Client

def get_notion(token:str)->Client:
    """
        Get the notion client using the token from the environment variables.
    """
    return Client(auth=token)