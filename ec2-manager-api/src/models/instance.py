from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict


class InstanceState(str, Enum):
    """Estados posibles de una instancia EC2"""
    PENDING = "pending"
    RUNNING = "running"
    SHUTTING_DOWN = "shutting-down"
    TERMINATED = "terminated"
    STOPPING = "stopping"
    STOPPED = "stopped"


class InstanceType(str, Enum):
    """Tipos de instancia EC2 más comunes"""
    T2_MICRO = "t2.micro"
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    T3_MICRO = "t3.micro"
    T3_SMALL = "t3.small"
    T3_MEDIUM = "t3.medium"
    M5_LARGE = "m5.large"
    M5_XLARGE = "m5.xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"


class AWSRegion(str, Enum):
    """Regiones AWS principales"""
    US_EAST_1 = "us-east-1"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    EU_CENTRAL_1 = "eu-central-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_NORTHEAST_1 = "ap-northeast-1"
    SA_EAST_1 = "sa-east-1"


class EC2Instance(BaseModel):
    """Modelo para una instancia EC2"""
    model_config = ConfigDict(use_enum_values=True)
    
    id: str
    name: str
    type: InstanceType
    state: InstanceState
    region: AWSRegion
    launch_time: Optional[str] = None
    private_ip: Optional[str] = None
    public_ip: Optional[str] = None


class StopInstanceResponse(BaseModel):
    """Respuesta para la operación de detener instancia"""
    model_config = ConfigDict(use_enum_values=True)
    
    success: bool
    message: str
    instance_id: str
    previous_state: InstanceState
    current_state: InstanceState


class ErrorResponse(BaseModel):
    """Respuesta de error estándar"""
    error: str
    message: str
    status_code: int
