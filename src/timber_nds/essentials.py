# essentials.py from timber_nds
from dataclasses import dataclass


@dataclass(frozen=True)
class WoodMaterial:
    name: str
    specific_gravity: float
    fibre_saturation_point: float
    tension_strength: float
    bending_strength: float
    shear_strength: float
    compression_perpendicular_strength: float
    compression_parallel_strength: float
    elastic_modulus: float
    color: str


@dataclass(frozen=True)
class RectangularSection:
    name: str
    depth: float
    width: float


@dataclass(frozen=True)
class MemberDefinition:
    name: str
    length: float
    effective_length_factor_yy: float
    effective_length_factor_zz: float

@dataclass(frozen=True)
class AdjustmentFactorsBase:
    pass

@dataclass(frozen=True)
class TensionAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_size: float
    due_incising: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class BendingAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_beam_stability: float
    due_size: float
    due_flat_use: float
    due_incising: float
    due_repetitive_member: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class ShearAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_incising: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class CompressionAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_size: float
    due_incising: float
    due_column_stability: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class PerpendicularAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_beam_stability: float
    due_size: float
    due_flat_use: float
    due_incising: float
    due_repetitive_member: float
    due_column_stability: float
    due_buckling_stiffness: float
    due_bearing_area: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class ElasticModulusAdjustmentFactors:
    due_moisture: float
    due_temperature: float
    due_incising: float
    due_format_conversion: float


@dataclass(frozen=True)
class Forces:
    axial_force: float
    shear_y: float
    shear_z: float
    moment_xx: float
    moment_yy: float
    moment_zz: float
