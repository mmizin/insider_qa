from typing import Optional


def create_pet_payload(id: int, name: str, category: Optional[dict] = None, photoUrls: Optional[list[str]] = None,
                       tags: Optional[list[dict]] = None, status: str = "available"):
    payload = {
        "id": id,
        "category": category or {
            "id": id,
            "name": name
        },
        "name": name,
        **({"photoUrls": photoUrls} if photoUrls else {}),
        "tags": tags or [
            {
                "id": id,
                "name": name
            }
        ],
        "status": status
    }
    
    return payload


def update_pet_payload(id: int, name: str, category: Optional[dict] = None, photoUrls: Optional[list[str]] = None,
                       tags: Optional[list[dict]] = None, status: str = "available"):
    default_tag = [{"id": id, "name": name}]
    default_category = {"id": id, "name": name}
    
    payload = {
        "id": id,
        "category": category or default_category,
        "name": name,
        **({"photoUrls": photoUrls} if photoUrls else {}),
        "tags": tags or default_tag,
        "status": status
    }
    
    return payload
