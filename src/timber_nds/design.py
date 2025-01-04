import timber_nds.src.timber_nds.essentials as essentials



class SummarizeFactors:
    """
    Calculates the weight of a wood element considering moisture content.

    Attributes:
        material (WoodProperties): Properties of the wood material.
        element (ElementProperties): Properties of the structural element.

    Methods:
        calculate_density_at_moisture_content(moisture_content) -> float:
            Calculates the density of the wood element considering its moisture content.
            Units: kg/m^3
        calculate_weight_at_moisture_content(moisture_content) -> float:
            Calculates the weight of the wood element considering its moisture content.
            Units: kg
    """

    def __init__(
        self,
        tension_factors:
        section: essentials.RectangularSection,
        element: essentials.MemberDefinition,
    ):
        self.material = material
        self.section = section
        self.element = element