"""
Timber NDS package initialization.
"""

__version__ = "0.1.0"

from . import essentials
from . import calculation
from . import design

from .essentials import (
    WoodMaterial,
    RectangularSection,
    MemberDefinition,
    TensionAdjustmentFactors,
    BendingAdjustmentFactors,
    ShearAdjustmentFactors,
    CompressionAdjustmentFactors,
    PerpendicularAdjustmentFactors,
    ElasticModulusAdjustmentFactors,
)
from .calculation import (
    WeightCalculator,
    effective_length,
    radius_of_gyration,
    polar_moment_of_inertia,
    RectangularSectionProperties,
)
from .design import (
    WoodElementCalculator,
)

__all__ = [
    "essentials",
    "calculation",
    "design",
    "WoodMaterial",
    "RectangularSection",
    "MemberDefinition",
    "TensionAdjustmentFactors",
    "BendingAdjustmentFactors",
    "ShearAdjustmentFactors",
    "CompressionAdjustmentFactors",
    "PerpendicularAdjustmentFactors",
    "ElasticModulusAdjustmentFactors",
    "WeightCalculator",
    "effective_length",
    "radius_of_gyration",
    "polar_moment_of_inertia",
    "RectangularSectionProperties",
    "WoodElementCalculator",
]
