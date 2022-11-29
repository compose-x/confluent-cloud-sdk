# generated by datamodel-codegen:
#   filename:  confluent-cloud-api.spec.json
#   timestamp: 2022-11-29T07:24:39+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra

class ConfluentCloudApiResourcesSpecifications(BaseModel):
    pass

    class Config:
        extra = Extra.forbid


class ApiVersion(BaseModel):
    __root__: str


class Id(BaseModel):
    __root__: str


class Kind(BaseModel):
    __root__: str


class ResourceMetadata(BaseModel):
    class Config:
        extra = Extra.forbid

    self: Optional[str] = None
    resource_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class SpecElement(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[Id] = None
    environment: Optional[str] = None
    related: Optional[str] = None
    resource_name: Optional[str] = None
    api_version: Optional[ApiVersion] = None
    kind: Optional[Kind] = None


class ListMetadata(BaseModel):
    class Config:
        extra = Extra.forbid

    first: Optional[str] = None
    last: Optional[str] = None
    prev: Optional[str] = None
    next: Optional[str] = None
    total_size: Optional[float] = None
