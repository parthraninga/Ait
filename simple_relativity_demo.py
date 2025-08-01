"""
Simple Relativity Demo - No Dependencies Required
A basic demonstration of relativity concepts using matplotlib animations

This version can run immediately without installing Manim.
For full-featured videos, use the Manim versions.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Rectangle
import time

class SimpleRelativityDemo:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_aspect('equal')
        self.ax.set_facecolor('black')
        
    def run_demo(self):
        """Run the complete demonstration"""
        self.title_screen()
        self.time_dilation_demo()
        self.length_contraction_demo()
        self.energy_mass_demo()
        self.spacetime_curvature_demo()
        self.conclusion()
        
    def title_screen(self):
        """Display title screen"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        # Title
        self.ax.text(0, 2, "Einstein's Theory of Relativity", 
                    fontsize=20, color='cyan', ha='center', weight='bold')
        self.ax.text(0, 1, "A Simple Animation Demo", 
                    fontsize=16, color='white', ha='center')
        self.ax.text(0, -1, "E = mc²", 
                    fontsize=24, color='gold', ha='center', weight='bold')
        self.ax.text(0, -3, "Press Enter to continue...", 
                    fontsize=12, color='gray', ha='center')
        
        # Add some decorative elements
        circle = Circle((0, 0), 4, fill=False, color='blue', alpha=0.3, linewidth=2)
        self.ax.add_patch(circle)
        
        # Stars
        for _ in range(20):
            x, y = np.random.uniform(-10, 10), np.random.uniform(-6, 6)
            self.ax.plot(x, y, '*', color='white', markersize=3)
        
        self.ax.axis('off')
        plt.title("Simple Relativity Demonstration", color='white', fontsize=16)
        plt.show(block=False)
        plt.pause(3)
        
    def time_dilation_demo(self):
        """Demonstrate time dilation with animated clocks"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        self.ax.text(0, 5, "Time Dilation", fontsize=18, color='red', ha='center', weight='bold')
        self.ax.text(0, 4, "Moving clocks run slower", fontsize=14, color='white', ha='center')
        
        # Stationary frame
        stationary_rect = Rectangle((-8, 1), 3, 2, fill=False, color='blue', linewidth=2)
        self.ax.add_patch(stationary_rect)
        self.ax.text(-6.5, 3.5, "Stationary Observer", color='blue', ha='center', fontsize=10)
        
        # Moving frame
        moving_rect = Rectangle((5, 1), 3, 2, fill=False, color='red', linewidth=2)
        self.ax.add_patch(moving_rect)
        self.ax.text(6.5, 3.5, "Moving at 0.8c", color='red', ha='center', fontsize=10)
        
        # Clock faces
        stat_clock = Circle((-6.5, 2), 0.8, fill=False, color='white', linewidth=2)
        mov_clock = Circle((6.5, 2), 0.8, fill=False, color='white', linewidth=2)
        self.ax.add_patch(stat_clock)
        self.ax.add_patch(mov_clock)
        
        # Animate clock hands
        stat_hand_line = None
        mov_hand_line = None
        
        for i in range(20):
            # Clear previous hands
            if stat_hand_line is not None:
                stat_hand_line.remove()
            if mov_hand_line is not None:
                mov_hand_line.remove()
            
            # Stationary clock hand (faster)
            stat_angle = i * np.pi / 5
            stat_x = -6.5 + 0.6 * np.cos(stat_angle - np.pi/2)
            stat_y = 2 + 0.6 * np.sin(stat_angle - np.pi/2)
            stat_hand_line = self.ax.plot([-6.5, stat_x], [2, stat_y], color='cyan', linewidth=3)[0]
            
            # Moving clock hand (slower due to time dilation)
            mov_angle = i * np.pi / 8  # Slower
            mov_x = 6.5 + 0.6 * np.cos(mov_angle - np.pi/2)
            mov_y = 2 + 0.6 * np.sin(mov_angle - np.pi/2)
            mov_hand_line = self.ax.plot([6.5, mov_x], [2, mov_y], color='orange', linewidth=3)[0]
            
            # Time dilation formula
            self.ax.text(0, -1, "Δt' = γΔt", fontsize=16, color='yellow', ha='center', weight='bold')
            self.ax.text(0, -2, "γ = 1/√(1 - v²/c²)", fontsize=12, color='yellow', ha='center')
            self.ax.text(0, -3, f"For v = 0.8c: γ = {1/np.sqrt(1-0.8**2):.2f}", 
                        fontsize=12, color='yellow', ha='center')
            
            self.ax.axis('off')
            plt.title("Time Dilation Demo", color='white', fontsize=16)
            plt.draw()
            plt.pause(0.3)
        
        plt.pause(2)
        
    def length_contraction_demo(self):
        """Demonstrate length contraction"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        self.ax.text(0, 5, "Length Contraction", fontsize=18, color='green', ha='center', weight='bold')
        self.ax.text(0, 4, "Moving objects appear shorter", fontsize=14, color='white', ha='center')
        
        # Rest length ruler
        rest_ruler = Rectangle((-4, 2), 8, 0.5, fill=True, color='blue', alpha=0.7)
        self.ax.add_patch(rest_ruler)
        self.ax.text(0, 3, "Ruler at Rest: L₀ = 8 units", color='blue', ha='center', fontsize=12)
        
        # Contracted ruler (moving)
        gamma = 1/np.sqrt(1-0.8**2)
        contracted_length = 8 / gamma
        contracted_ruler = Rectangle((-contracted_length/2, 0), contracted_length, 0.5, 
                                   fill=True, color='red', alpha=0.7)
        self.ax.add_patch(contracted_ruler)
        self.ax.text(0, 1, f"Same Ruler Moving: L = L₀/γ = {contracted_length:.1f} units", 
                    color='red', ha='center', fontsize=12)
        
        # Motion lines
        for x in np.linspace(-3, 3, 10):
            self.ax.plot([x-0.5, x+0.5], [-0.5, -0.5], color='yellow', linewidth=1, alpha=0.7)
        
        # Formula
        self.ax.text(0, -2, "L = L₀/γ = L₀√(1 - v²/c²)", 
                    fontsize=14, color='yellow', ha='center', weight='bold')
        self.ax.text(0, -3, f"For v = 0.8c: L = L₀ × {1/gamma:.2f}", 
                    fontsize=12, color='yellow', ha='center')
        
        self.ax.axis('off')
        plt.title("Length Contraction Demo", color='white', fontsize=16)
        plt.draw()
        plt.pause(3)
        
    def energy_mass_demo(self):
        """Demonstrate E=mc²"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        self.ax.text(0, 5, "Mass-Energy Equivalence", fontsize=18, color='purple', ha='center', weight='bold')
        
        # Small mass
        mass_circle = Circle((-5, 0), 0.5, fill=True, color='white', alpha=0.8)
        self.ax.add_patch(mass_circle)
        self.ax.text(-5, -1.5, "Small Mass (m)", color='white', ha='center', fontsize=12)
        
        # Arrow
        self.ax.arrow(-3, 0, 2, 0, head_width=0.3, head_length=0.5, fc='yellow', ec='yellow')
        self.ax.text(-2, 0.5, "×c²", color='yellow', ha='center', fontsize=14, weight='bold')
        
        # Huge energy
        energy_circle = Circle((5, 0), 2, fill=True, color='gold', alpha=0.5)
        self.ax.add_patch(energy_circle)
        self.ax.text(5, -3, "ENORMOUS Energy!", color='gold', ha='center', fontsize=12, weight='bold')
        
        # The famous equation
        self.ax.text(0, 2, "E = mc²", fontsize=32, color='gold', ha='center', weight='bold')
        
        # Example calculation
        self.ax.text(0, -4, "Example: 1 gram of matter = 90 trillion joules", 
                    color='cyan', ha='center', fontsize=10)
        self.ax.text(0, -4.5, "(Enough energy to power a city for hours!)", 
                    color='cyan', ha='center', fontsize=10, style='italic')
        
        self.ax.axis('off')
        plt.title("E = mc² Demonstration", color='white', fontsize=16)
        plt.draw()
        plt.pause(3)
        
    def spacetime_curvature_demo(self):
        """Demonstrate spacetime curvature"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        self.ax.text(0, 5, "Spacetime Curvature", fontsize=18, color='orange', ha='center', weight='bold')
        self.ax.text(0, 4, "Mass curves spacetime", fontsize=14, color='white', ha='center')
        
        # Create grid
        x = np.linspace(-8, 8, 17)
        y = np.linspace(-4, 4, 9)
        
        # Draw curved grid around central mass
        for i in range(len(x)):
            for j in range(len(y)):
                if np.sqrt(x[i]**2 + y[j]**2) > 1.5:  # Don't draw inside the mass
                    # Apply curvature effect
                    r = np.sqrt(x[i]**2 + y[j]**2)
                    curvature = 0.5 / r if r > 0.1 else 0
                    curved_y = y[j] - curvature
                    
                    self.ax.plot(x[i], curved_y, 'o', color='blue', markersize=2, alpha=0.6)
        
        # Central mass (star)
        star = Circle((0, 0), 1, fill=True, color='yellow', alpha=0.9)
        self.ax.add_patch(star)
        self.ax.text(0, 0, "⭐", fontsize=20, ha='center', va='center')
        
        # Orbital path
        theta = np.linspace(0, 2*np.pi, 100)
        orbit_x = 4 * np.cos(theta)
        orbit_y = 2 * np.sin(theta)
        self.ax.plot(orbit_x, orbit_y, '--', color='green', linewidth=2, alpha=0.7)
        
        # Planet
        planet = Circle((4, 0), 0.3, fill=True, color='blue', alpha=0.8)
        self.ax.add_patch(planet)
        
        # Einstein's field equation
        self.ax.text(0, -4, "Gμν = (8πG/c⁴)Tμν", fontsize=12, color='yellow', ha='center', weight='bold')
        self.ax.text(0, -4.5, "Einstein's Field Equation", color='yellow', ha='center', fontsize=10)
        
        self.ax.axis('off')
        plt.title("General Relativity: Spacetime Curvature", color='white', fontsize=16)
        plt.draw()
        plt.pause(3)
        
    def conclusion(self):
        """Display conclusion"""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-6, 6)
        self.ax.set_facecolor('black')
        
        self.ax.text(0, 4, "Einstein's Revolutionary Ideas", 
                    fontsize=18, color='green', ha='center', weight='bold')
        
        conclusions = [
            "• Time and space are relative",
            "• Nothing travels faster than light",
            "• Mass and energy are equivalent",
            "• Gravity curves spacetime",
            "• These effects are real and measurable!"
        ]
        
        for i, conclusion in enumerate(conclusions):
            self.ax.text(0, 2-i*0.8, conclusion, fontsize=14, color='white', ha='center')
        
        self.ax.text(0, -4, '"Imagination is more important than knowledge"', 
                    fontsize=12, color='yellow', ha='center', style='italic')
        self.ax.text(0, -4.5, "- Albert Einstein", 
                    fontsize=10, color='yellow', ha='center')
        
        # Add decorative elements
        for _ in range(30):
            x, y = np.random.uniform(-10, 10), np.random.uniform(-6, 6)
            self.ax.plot(x, y, '*', color='white', markersize=2, alpha=0.5)
        
        self.ax.axis('off')
        plt.title("Thank you for watching!", color='white', fontsize=16)
        plt.draw()
        plt.pause(5)

def create_interactive_demo():
    """Create an interactive demonstration"""
    def relativistic_calculator():
        """Calculate relativistic effects for given velocity"""
        print("\n" + "="*50)
        print("RELATIVISTIC EFFECTS CALCULATOR")
        print("="*50)
        
        try:
            v_fraction = float(input("Enter velocity as fraction of c (0-0.99): "))
            if v_fraction >= 1 or v_fraction < 0:
                print("Velocity must be between 0 and 0.99c")
                return
            
            gamma = 1 / np.sqrt(1 - v_fraction**2)
            
            print(f"\nFor velocity = {v_fraction:.2f}c:")
            print(f"Lorentz factor (γ) = {gamma:.3f}")
            print(f"Time dilation: Time runs {gamma:.2f}x slower")
            print(f"Length contraction: Length is {1/gamma:.3f}x shorter")
            print(f"Relativistic mass increase: {gamma:.2f}x rest mass")
            
            # Energy calculation for 1 kg
            c = 299792458  # m/s
            rest_energy = c**2  # J (for 1 kg)
            total_energy = gamma * rest_energy
            kinetic_energy = total_energy - rest_energy
            
            print(f"\nFor 1 kg object:")
            print(f"Rest energy: {rest_energy:.2e} J")
            print(f"Total energy: {total_energy:.2e} J")
            print(f"Kinetic energy: {kinetic_energy:.2e} J")
            
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        print("\n" + "="*50)
        print("EINSTEIN'S RELATIVITY DEMONSTRATION")
        print("="*50)
        print("1. Run visual demonstration")
        print("2. Relativistic calculator")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            demo = SimpleRelativityDemo()
            demo.run_demo()
        elif choice == '2':
            relativistic_calculator()
        elif choice == '3':
            print("Thank you for exploring relativity!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    print("Einstein's Theory of Relativity - Simple Demo")
    print("This is a basic version using matplotlib.")
    print("For professional-quality videos, install Manim and run the other scripts.")
    print("\nStarting interactive demonstration...")
    
    create_interactive_demo()
