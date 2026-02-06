import math

A0 = 1.129e-10 

def get_grest_response(g_n):
    return math.sqrt(g_n**2 + (g_n * A0))

def main():
    print("--- GREST UNIVERSAL CALCULATOR ---")
    try:
        gn_input = float(input("Enter Newtonian Acceleration (g_n): "))
        g_obs = get_grest_response(gn_input)
        print(f"\nGREST g_obs: {g_obs:.2e} m/s^2")
        
        r_val = input("\nEnter Radius (m) for Velocity [or skip]: ")
        if r_val:
            v = math.sqrt(g_obs * float(r_val))
            print(f"Orbital Velocity: {v/1000:.2f} km/s")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()