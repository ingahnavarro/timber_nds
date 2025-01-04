from dataclasses import dataclass


@dataclass(frozen=True)
class WoodMaterial:
    """
    Represents basic material properties.

    Attributes:
        name: Material name.
        specific_gravity:
        elastic_modulus: Modulus of elasticity (Young's modulus).
        ...
        color: Color associated with the material.
    """
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
    """
    Represents a rectangular section.

    Attributes:
        name: Name or identifier of the rectangular section.
        depth: Depth (height) of the rectangular section.
        width: Width of the rectangular section.
    """
    name: str
    depth: float
    width: float


@dataclass(frozen=True)
class MemberDefinition:
    """
    Represents the definition of a structural member.

    Attributes:
        element_name: Name or identifier of the structural element.
        element_length: Length of the structural element.
        effective_length_factor_yy: Effective length factor along the yy-axis.
        effective_length_factor_zz: Effective length factor along the zz-axis.
    """
    name: str
    length: float
    effective_length_factor_yy: float
    effective_length_factor_zz: float


@dataclass(frozen=True)
class TensionAdjustmentFactors:
    """Represents adjustment factors for sawn lumber in tension.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_size: Reduction factor due to size.
        due_incising: Reduction factor due to incising.
        due_format_conversion: Reduction factor due to format conversion.
        due_resistance_reduction: Reduction factor due to general resistance reduction.
        due_time_effect: Reduction factor due to time effect.
    """

    due_moisture: float
    due_temperature: float
    due_size: float
    due_incising: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class BendingAdjustmentFactors:
    """Represents adjustment factors for sawn lumber in bending.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_beam_stability: Reduction factor due to beam stability.
        due_size: Reduction factor due to size.
        due_flat_use: Reduction factor due to flat use.
        due_incising: Reduction factor due to incising.
        due_repetitive_member: Reduction factor due to repetitive member.
        due_format_conversion: Reduction factor due to format conversion.
        due_resistance_reduction: Reduction factor due to general resistance reduction.
        due_time_effect: Reduction factor due to time effect.
    """

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
    """Represents adjustment factors for sawn lumber in shear.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_incising: Reduction factor due to incising.
        due_format_conversion: Reduction factor due to format conversion.
        due_resistance_reduction: Reduction factor due to general resistance reduction.
        due_time_effect: Reduction factor due to time effect.
    """

    due_moisture: float
    due_temperature: float
    due_incising: float
    due_format_conversion: float
    due_resistance_reduction: float
    due_time_effect: float


@dataclass(frozen=True)
class CompressionAdjustmentFactors:
    """Represents adjustment factors for sawn lumber in parallel compression.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_size: Reduction factor due to size.
        due_incising: Reduction factor due to incising.
        due_column_stability: Reduction factor due to column stability.
        due_format_conversion: Reduction factor due to format conversion.
        due_resistance_reduction: Reduction factor due to general resistance reduction.
        due_time_effect: Reduction factor due to time effect.
    """

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
    """Represents adjustment factors for sawn lumber in perpendicular compression.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_beam_stability: Reduction factor due to beam stability.
        due_size: Reduction factor due to size.
        due_flat_use: Reduction factor due to flat use.
        due_incising: Reduction factor due to incising.
        due_repetitive_member: Reduction factor due to repetitive member.
        due_column_stability: Reduction factor due to column stability.
        due_buckling_stiffness: Reduction factor due to buckling stiffness.
        due_bearing_area: Reduction factor due to bearing area.
        due_format_conversion: Reduction factor due to format conversion.
        due_resistance_reduction: Reduction factor due to general resistance reduction.
        due_time_effect: Reduction factor due to time effect.
    """

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
    """Represents adjustment factors for the elastic modulus of sawn lumber.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_incising: Reduction factor due to incising.
    """

    due_moisture: float
    due_temperature: float
    due_incising: float


@dataclass(frozen=True)
class MinModulusAdjustmentFactors:
    """Represents adjustment factors for the minimum modulus of sawn lumber.

    Attributes:
        due_moisture: Reduction factor due to service moisture content.
        due_temperature: Reduction factor due to temperature.
        due_incising: Reduction factor due to incising.
        buckling_stiffness: Reduction factor for buckling stiffness.
    """

    due_moisture: float
    due_temperature: float
    due_incising: float
    buckling_stiffness: float


@dataclass(frozen=True)
class Forces:
    """
    Represents a set of forces and moments acting on a structural element.

    Attributes:
        axial_force: Axial force.
        shear_y: Shear force in the y-axis.
        shear_z: Shear force in the z-axis.
        moment_xx: Torsional moment about the x-axis.
        moment_yy: Bending moment about the y-axis.
        moment_zz: Bending moment about the z-axis.
    """
    axial_force: float
    shear_y: float
    shear_z: float
    moment_xx: float
    moment_yy: float
    moment_zz: float
