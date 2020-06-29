from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class NavigationItem:
    raw_url: str
    label: str

    items: Optional[List['NavigationItem']] = None
    is_active: bool = False

    def __str__(self):
        return f'{self.label}'
