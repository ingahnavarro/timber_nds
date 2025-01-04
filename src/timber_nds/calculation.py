import numpy as np
import timber_nds.src.timber_nds.essentials as essentials


class WeightCalculator:
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
        material: essentials.WoodMaterial,
        section: essentials.RectangularSection,
        element: essentials.MemberDefinition,
    ):
        self.material = material
        self.section = section
        self.element = element

    def calculate_density_at_moisture_content(self, moisture_content: float) -> float:
        """
        Calculates the density of the wood element at a given moisture content.

        Args:
            moisture_content: The moisture content of the wood, as a percentage.

        Returns:
            The density of the wood element in kg/m^3.

        Assumptions:
            - The moisture content is given as a percentage (e.g., 12.5 for 12.5%).
            - Density of water is 1000 kg/m^3
        """
        if not isinstance(moisture_content, (int, float)):
            raise TypeError("Moisture content must be a number (int or float)")
        if moisture_content < 0:
            raise ValueError("Moisture content must be non-negative.")
        if self.material.fibre_saturation_point < 0:
            raise ValueError("Fibre saturation point must be non-negative.")

        if moisture_content <= self.material.fibre_saturation_point:
            density_at_moisture = (
                self.material.specific_gravity
                * 1000
                * ((moisture_content / 100) + 1)
                / (
                    (self.material.fibre_saturation_point / 100)
                    * self.material.specific_gravity
                    + 1
                )
            )
        else:
            density_at_moisture = (
                self.material.specific_gravity
                * 1000
                * (
                    (self.material.fibre_saturation_point / 100)
                    + 1
                )
                / (
                    (self.material.fibre_saturation_point / 100)
                    * self.material.specific_gravity
                    + 1
                )
            )
        return density_at_moisture

    def calculate_weight_at_moisture_content(self, moisture_content: float) -> float:
        """
        Calculates the weight of the wood element at a given moisture content.

        Args:
            moisture_content: The moisture content of the wood, as a percentage.

        Returns:
            The weight of the wood element in kg.

        Assumptions:
           - The provided dimensions are valid (positive).
        """

        if not isinstance(moisture_content, (int, float)):
            raise TypeError("Moisture content must be a number (int or float)")
        if moisture_content < 0:
            raise ValueError("Moisture content must be non-negative.")
        if self.section.width < 0 or self.section.depth < 0 or self.element.length < 0:
            raise ValueError("Element dimensions must be non-negative values.")

        volume = self.section.width * self.section.depth * self.element.length
        density = self.calculate_density_at_moisture_content(moisture_content)
        weight = volume * density
        return weight


def effective_length(k_factor: float, length: float) -> float:
    """
    Calculates the effective length of a member.

    Args:
        k_factor: Effective length factor (K).
        length: Length of the element.

    Returns:
        The effective length of the member.
    """
    return k_factor * length


def radius_of_gyration(i: float, area: float) -> float:
    """
    Calculates the radius of gyration for any section.

    Args:
        i: Second moment of area (I).
        area: Area of the section (A).

    Returns:
        The radius of gyration.

    Raises:
        ValueError: If the area is zero.
    """
    if area == 0:
        raise ValueError("Area cannot be zero.")
    return np.sqrt(i / area)


def polar_moment_of_inertia(i_yy: float, i_zz: float) -> float:
    """
    Calculates the polar moment of inertia for any section.

    Args:
        i_yy: Second moment of area about the yy axis (Ix).
        i_zz: Second moment of area about the zz axis (Iy).

    Returns:
        The polar moment of inertia.
    """
    return i_yy + i_zz


class RectangularSectionProperties:
    """
    Represents properties of a rectangular section.

    Attributes:
        width: Width of the section.
        depth: Depth of the section.
    """

    def __init__(self, width: float, depth: float):
        self.width = width
        self.depth = depth

    def area(self) -> float:
        """
        Calculates the area.

        Returns:
            The area.
        """
        return self.width * self.depth

    def i_yy(self) -> float:
        """
        Calculates the second moment of area about the yy axis.

        Returns:
            The second moment of area.
        """
        return (self.width * self.depth**3) / 12

    def i_zz(self) -> float:
        """
        Calculates the second moment of area about the zz axis.

        Returns:
            The second moment of area.
        """
        return (self.depth * self.width**3) / 12

    def elastic_section_modulus_yy(self) -> float:
        """
        Calculates the elastic section modulus about the yy axis.

        Returns:
            The elastic section modulus.
        """
        return (self.width * self.depth**2) / 6

    def elastic_section_modulus_zz(self) -> float:
        """
        Calculates the elastic section modulus about the zz axis.

        Returns:
            The elastic section modulus.
        """
        return (self.depth * self.width**2) / 6

    def plastic_section_modulus_yy(self) -> float:
        """
        Calculates the plastic section modulus about the yy axis.

        Returns:
            The plastic section modulus.
        """
        return (self.width * self.depth**2) / 4

    def plastic_section_modulus_zz(self) -> float:
        """
        Calculates the plastic section modulus about the zz axis.

        Returns:
            The plastic section modulus.
        """
        return (self.depth * self.width**2) / 4

    def polar_moment_of_inertia(self) -> float:
        """
        Calculates the polar moment of inertia.

        Returns:
            The polar moment of inertia.
        """
        return self.i_yy() + self.i_zz()

    def radius_of_gyration_yy(self) -> float:
        """
        Calculates the radius of gyration about the yy axis.

        Returns:
            The radius of gyration.
        """
        return radius_of_gyration(self.i_yy(), self.area())

    def radius_of_gyration_zz(self) -> float:
        """
        Calculates the radius of gyration about the zz axis.

        Returns:
            The radius of gyration.
        """
        return radius_of_gyration(self.i_zz(), self.area())
