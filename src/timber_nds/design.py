# design.py from timber_nds
import numpy as np
import timber_nds.essentials as te
import timber_nds.calculation as tc


class WoodElementCalculator:
    """Calculates the adjusted strength of a wood element.

    Args:
        tension_factors: Adjustment factors for tension.
        bending_factors_yy or bending_factors_zz: Adjustment factors for bending around "yy" or "zz".
        shear_factors: Adjustment factors for shear.
        compression_factors_yy or compression_factors_zz: Adjustment factors for compression with buckling around "yy" or "zz".
        compression_perp_factors: Adjustment factors for compression perpendicular to grain.
        elastic_modulus_factors: Adjustment factors for the modulus of elasticity.
        material_properties: Wood material properties.
        section_properties: Wood section properties.

    Returns:
        None

    Assumptions:
        All input factors are positive numerical values.
        Each set of factors (e.g., tension, bending) is consistent in terms of units.
    """

    def __init__(
            self,
            tension_factors: te.TensionAdjustmentFactors,
            bending_factors_yy: te.BendingAdjustmentFactors,
            bending_factors_zz: te.BendingAdjustmentFactors,
            shear_factors: te.ShearAdjustmentFactors,
            compression_factors_yy: te.CompressionAdjustmentFactors,
            compression_factors_zz: te.CompressionAdjustmentFactors,
            compression_perp_factors: te.PerpendicularAdjustmentFactors,
            elastic_modulus_factors: te.ElasticModulusAdjustmentFactors,
            material_properties: te.WoodMaterial,
            section_properties: tc.RectangularSectionProperties,
    ):

        self.tension_factors = tension_factors
        self.bending_factors_yy = bending_factors_yy
        self.bending_factors_zz = bending_factors_zz
        self.shear_factors = shear_factors
        self.compression_factors_yy = compression_factors_yy
        self.compression_factors_zz = compression_factors_zz
        self.compression_perp_factors = compression_perp_factors
        self.elastic_modulus_factors = elastic_modulus_factors
        self.material_properties = material_properties
        self.section_properties = section_properties

    def calculate_combined_factors(self) -> dict:
        """
        Calculates combined factors.

        Returns:
            Dictionary of combined factors.
        """
        try:
            tension_combined = np.prod(list(self.tension_factors.__dict__.values()))
            bending_combined_yy = np.prod(list(self.bending_factors_yy.__dict__.values()))
            bending_combined_zz = np.prod(list(self.bending_factors_zz.__dict__.values()))
            shear_combined = np.prod(list(self.shear_factors.__dict__.values()))
            compression_combined_yy = np.prod(list(self.compression_factors_yy.__dict__.values()))
            compression_combined_zz = np.prod(list(self.compression_factors_zz.__dict__.values()))
            compression_perp_combined = np.prod(list(self.compression_perp_factors.__dict__.values()))
            elastic_modulus_combined = np.prod(list(self.elastic_modulus_factors.__dict__.values()))
        except TypeError as e:
            raise TypeError(f"All factor values must be numeric: {e}") from e

        return {
            "tension": tension_combined,
            "bending_yy": bending_combined_yy,
            "bending_zz": bending_combined_zz,
            "shear": shear_combined,
            "compression_yy": compression_combined_yy,
            "compression_zz": compression_combined_zz,
            "compression_perp": compression_perp_combined,
            "elastic_modulus": elastic_modulus_combined,
        }

    def section_tension_strength(self) -> float:
        """Calculates the adjusted tension strength.

        Returns:
            Adjusted tension strength of the wood section.

        Assumptions:
            Connection effects are not included.
        """

        return (
            self.material_properties.tension_strength
            * self.section_properties.area()
            * self.calculate_combined_factors()["tension"]
        )

    def section_bending_strength(self, direction: str) -> float:
        """Calculates the adjusted bending strength.

        Args:
            direction: Bending direction ("yy" or "zz").

        Returns:
            Adjusted bending strength.

        Assumptions:
            Connection effects are not included.
        """
        if direction == "yy":
            bending_strength = (
                    self.material_properties.bending_strength
                    * self.section_properties.elastic_section_modulus(direction)
                    * self.calculate_combined_factors()["bending_yy"]
            )
        elif direction == "zz":
            bending_strength = (
                    self.material_properties.bending_strength
                    * self.section_properties.elastic_section_modulus(direction)
                    * self.calculate_combined_factors()["bending_zz"]
            )
        else:
            raise ValueError("Invalid direction. Use 'yy' or 'zz'.")

        return bending_strength

    def section_shear_strength(self) -> float:
        """Calculates the adjusted bending strength about yy axis.

        Returns:
            Adjusted shear strength.

        Assumptions:
            Connection effects are not included.
        """

        return (
            2/3
            * self.material_properties.shear_strength
            * self.section_properties.area()
            * self.calculate_combined_factors()["shear"]
        )

    def section_compression_strength(self, direction: str) -> float:
        """Calculates the adjusted tension strength.

        Returns:
            Adjusted compression strength of the wood section.

        Assumptions:
            Connection effects are not included.
        """
        if direction == "yy":
            compression_parallel_strength = (
                self.material_properties.compression_parallel_strength
                * self.section_properties.elastic_section_modulus(direction)
                * self.calculate_combined_factors()["compression_yy"]
            )
        elif direction == "zz":
            compression_parallel_strength = (
                self.material_properties.compression_parallel_strength
                * self.section_properties.elastic_section_modulus(direction)
                * self.calculate_combined_factors()["compression_zz"]
            )
        else:
            raise ValueError("Invalid direction. Use 'yy' or 'zz'.")

        return compression_parallel_strength

    def section_compression_perp_strength(self) -> float:
        """Calculates the adjusted tension strength. ff

        Returns:
            Adjusted tension strength of the wood section.

        Assumptions:
            Connection effects are not included.
        """

        return (
            self.material_properties.tension_strength
            * self.section_properties.area()
            * self.calculate_combined_factors()["compression_perp"]
        )
