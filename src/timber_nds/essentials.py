from dataclasses import dataclass


@dataclass
class WoodMaterial:
    name: str = "Default Wood"
    specific_gravity: float = 0.6
    fibre_saturation_point: float = 0.25
    tension_strength: float = 10.0
    bending_strength: float = 15.0
    shear_strength: float = 2.5
    compression_perpendicular_strength: float = 3.0
    compression_parallel_strength: float = 12.0
    elastic_modulus: float = 10000.0
    color: str = "Brown"


@dataclass
class RectangularSection:
    name: str = "Default Section"
    depth: float = 200.0
    width: float = 100.0


@dataclass
class MemberDefinition:
    name: str = "Default Member"
    length: float = 3000.0
    effective_length_factor_yy: float = 1.0
    effective_length_factor_zz: float = 1.0


@dataclass
class TensionAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_size: float = 1.0
    due_incising: float = 1.0
    due_format_conversion: float = 1.0
    due_resistance_reduction: float = 1.0
    due_time_effect: float = 1.0


@dataclass
class BendingAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_beam_stability: float = 1.0
    due_size: float = 1.0
    due_flat_use: float = 1.0
    due_incising: float = 1.0
    due_repetitive_member: float = 1.0
    due_format_conversion: float = 1.0
    due_resistance_reduction: float = 1.0
    due_time_effect: float = 1.0


@dataclass
class ShearAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_incising: float = 1.0
    due_format_conversion: float = 1.0
    due_resistance_reduction: float = 1.0
    due_time_effect: float = 1.0


@dataclass
class CompressionAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_size: float = 1.0
    due_incising: float = 1.0
    due_column_stability: float = 1.0
    due_format_conversion: float = 1.0
    due_resistance_reduction: float = 1.0
    due_time_effect: float = 1.0


@dataclass
class PerpendicularAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_beam_stability: float = 1.0
    due_size: float = 1.0
    due_flat_use: float = 1.0
    due_incising: float = 1.0
    due_repetitive_member: float = 1.0
    due_column_stability: float = 1.0
    due_buckling_stiffness: float = 1.0
    due_bearing_area: float = 1.0
    due_format_conversion: float = 1.0
    due_resistance_reduction: float = 1.0
    due_time_effect: float = 1.0


@dataclass
class ElasticModulusAdjustmentFactors:
    due_moisture: float = 1.0
    due_temperature: float = 1.0
    due_incising: float = 1.0
    due_format_conversion: float = 1.0


@dataclass
class Forces:
    axial_force: float = 0.0
    shear_y: float = 0.0
    shear_z: float = 0.0
    moment_xx: float = 0.0
    moment_yy: float = 0.0
    moment_zz: float = 0.0
