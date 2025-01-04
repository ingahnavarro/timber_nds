import unittest


class TestStructuralFunctions(unittest.TestCase):
    def test_effective_length(self):
        self.assertEqual(effective_length(2.0, 5.0), 10.0)
        self.assertEqual(effective_length(1.0, 10.0), 10.0)
        self.assertEqual(effective_length(0.5, 20.0), 10.0)

    def test_radius_of_gyration(self):
        self.assertEqual(radius_of_gyration(4.0, 4.0), 1.0)
        self.assertEqual(radius_of_gyration(16.0, 4.0), 2.0)

        with self.assertRaises(ValueError):
            radius_of_gyration(1.0, 0.0)

    def test_polar_moment_of_inertia(self):
        self.assertEqual(polar_moment_of_inertia(4.0, 6.0), 10.0)
        self.assertEqual(polar_moment_of_inertia(10.0, 0.0), 10.0)

    def test_rectangular_section_properties(self):
        section = RectangularSectionProperties(width=2.0, depth=3.0)
        self.assertEqual(section.area(), 6.0)
        self.assertEqual(section.i_yy(), 4.5)
        self.assertEqual(section.i_zz(), 1.5)
        self.assertEqual(section.elastic_section_modulus_yy(), 3.0)
        self.assertEqual(section.elastic_section_modulus_zz(), 2.0)
        self.assertEqual(section.plastic_section_modulus_yy(), 4.5)
        self.assertEqual(section.plastic_section_modulus_zz(), 3.0)
        self.assertEqual(section.polar_moment_of_inertia(), 6.0)
        self.assertAlmostEqual(section.radius_of_gyration_yy(), 0.8660254, places=6)  # Using assertAlmostEqual for float comparison
        self.assertAlmostEqual(section.radius_of_gyration_zz(), 0.5, places=6)     # Using assertAlmostEqual for float comparison


if __name__ == "__main__":
    unittest.main()
    