from dataclasses import dataclass, field
from typing import List, Optional

from pydantic import BaseModel


@dataclass
class LogicalTable:
    name: str
    localized: bool
    id_type: str
    inverse_fks: bool
    valid_type: str
    internal: bool
    historized: bool
    pk: str
    attributes: list
    all_columns: list
    old_audit: bool
    ties: list
    blocks: Optional[list] = field(default_factory=lambda: [])
    field_blocks: Optional[list] = field(default_factory=lambda: [])
    tags: Optional[list] = field(default_factory=lambda: [])
    backrefs: Optional[list] = field(default_factory=lambda: [])
    virtual_attributes: Optional[list] = field(default_factory=lambda: [])
    indexes: Optional[list] = field(default_factory=lambda: [])
    unique_indexes: Optional[list] = field(default_factory=lambda: [])


@dataclass
class LogicalColumn:
    name: str
    db_name: str
    default: Optional[str]
    localized: bool
    valid_type: str
    type: str
    serial_type: Optional[str]
    nullable: bool
    fk: Optional[str]
    unique: bool
    pk: bool
    enum: Optional[str]
    tags: list
    description: Optional[str] = ""


@dataclass
class LogicalTie:
    name: str
    valid_type: str
    fks: list


@dataclass
class TableTieRelation:
    name: str
    relation_name: str
    other: str


@dataclass
class LogicalEnum:
    name: str
    id_type: str
    valid_type: str
    coded: bool
    localized: bool
    values: list
    values_localized: list


@dataclass
class ForeignKey:
    table: str
    ref_id: str
    name: str


@dataclass
class InverseForeignKey:
    table: str
    valid_type: str
    name: str


@dataclass
class BlockElement:
    value: str
    type: str


@dataclass
class VirtualAttribute:
    name: str
    type: str


@dataclass
class SystemDefinition:
    attributes: list
    aces: list
    global_aces: list


@dataclass
class Backref:
    attribute: str
    ref_table: str
    ref_id: str
    ref_type: str
