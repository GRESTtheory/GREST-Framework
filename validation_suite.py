import math
import csv

A0 = 1.129e-10 

def run_validation():
    print("--- GREST AUTOMATED VALIDATION SUITE ---")
    print(f"{'System':<25} | {'Observed':<12} | {'Predicted':<12} | {'Accuracy'}")
    print("-" * 70)
    total_acc = 0
    count = 0
    
    try:
        with open('systems_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obs = float(row['Observed_Value'])
                pred = float(row['GREST_Predicted'])
                acc = float(row['Accuracy_Pct'])
                
                total_acc += acc
                count += 1
                print(f"{row['System']:<25} | {obs:<12} | {pred:<12} | {acc}%")
        
        print("-" * 70)
        print(f"FINAL MEAN ACCURACY: {total_acc / count:.2f}%")
    except FileNotFoundError:
        print("Error: systems_data.csv not found.")

if __name__ == "__main__":
    run_validation()