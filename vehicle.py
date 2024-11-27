vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
        }

def main():
  vin = input("Please enter the VIN of the vehicle: ")
  if vin in vehicles:
    vehicle_info=vehicles[vin]
    print(f"The year of the vehicle is {vehicle_info[0]}")
    print(f"The manufacturer of the vehicle is {vehicle_info[1]}")
    print(f"The model of the vehicle is {vehicle_info[2]}")
    print(f"The color of the vehicle is {vehicle_info[3]}")
    print(f"The design of the vehicle is {vehicle_info[4]}")
    print(f"The displace of the vehicle is {vehicle_info[5]}")

  else:
    print("Invalid VIN")
if __name__ == "__main__":

    main()
        
        
        
    
