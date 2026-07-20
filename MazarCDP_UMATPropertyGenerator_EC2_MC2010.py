# Developer: Engr. Tufail Mabood
# WhatsApp: +923440907874

import os
import math
import pandas as pd


def compute_concrete_properties(fck):
    """Compute concrete properties according to EC2 and MC2010 for a given fck (MPa)."""

    fcm = fck + 8
    E = 22 * (fcm / 10) ** 0.3 * 1000
    nu = 0.20

    if fck <= 50:
        fctm = 0.3 * fck ** (2 / 3)
    else:
        fctm = 2.12 * math.log(1 + fcm / 10)

    GfIt = 73 * (fcm / 10) ** 0.18
    GfIc = 100 * GfIt
    ec1 = 0.7 * fcm ** 0.31 / 1000

    if fck <= 50:
        ecu1 = 0.0022
    elif 50 < fck <= 90:
        ecu1 = (2.6 + 35 * ((90 - fck) / 100) ** 4) / 1000
    else:
        ecu1 = 0.0026

    return {
        "props(1)": E,
        "props(2)": nu,
        "props(3)": fctm,
        "props(4)": 0.0,
        "props(5)": GfIt,
        "props(6)": GfIc,
        "props(7)": 0.0,
        "props(8)": 0.001,
        "props(9)": 1.0,
        "props(10)": 1.0,
        "props(11)": 0.0,
        "props(12)": 0.1,
        "props(13)": 0.1,
        "props(14)": 0.0,
        "props(15)": 0.0,
        "props(16)": 0.0,
        "props(17)": 0.0,
        "props(18)": 0.0,
        "props(19)": ec1,
        "props(20)": ecu1,
        "props(21)": fcm
    }


def save_to_file(fck, file_format="xlsx"):
    """
    Save computed concrete properties to a spreadsheet.

    Supported formats:
        - xlsx : Microsoft Excel (.xlsx)
        - ods  : OpenDocument Spreadsheet (.ods) for LibreOffice/OpenOffice

    XLSX remains the default format for backward compatibility.
    """

    psi_strength = round(fck * 145.038, 2)
    props = compute_concrete_properties(fck)

    df = pd.DataFrame(props.items(), columns=["Property", "Value"])

    file_name = f"fck_{fck}MPa_{psi_strength}PSI.{file_format}"
    file_path = os.path.join(os.getcwd(), file_name)

    # Added support for OpenDocument Spreadsheet (.ods) format.
    # This allows LibreOffice/OpenOffice users to open the generated
    # files natively while preserving existing Excel (.xlsx) support.
    if file_format == "xlsx":
        df.to_excel(file_path, index=False)

    elif file_format == "ods":
        # The 'odf' engine requires the optional 'odfpy' package:
        #     pip install odfpy
        df.to_excel(file_path, engine="odf", index=False)

    else:
        raise ValueError("Unsupported file format. Choose 'xlsx' or 'ods'.")

    print(f"\nFile saved: {file_name}")
    print(f"Location : {os.getcwd()}")


if __name__ == "__main__":
    try:
        fck_input = float(input("Enter the concrete strength (fck) in MPa: "))

        if 1 <= fck_input <= 200:

            # Added format selection.
            # Default remains XLSX to maintain backward compatibility,
            # while also allowing users to generate LibreOffice (.ods)
            # files or both formats simultaneously.
            fmt = input(
                "Choose output format (xlsx/ods/both) [xlsx]: "
            ).strip().lower()

            if fmt == "":
                fmt = "xlsx"

            if fmt == "xlsx":
                save_to_file(fck_input, "xlsx")

            elif fmt == "ods":
                save_to_file(fck_input, "ods")

            elif fmt == "both":
                # Export both spreadsheet formats.
                save_to_file(fck_input, "xlsx")
                save_to_file(fck_input, "ods")

            else:
                print("Invalid format! Please choose xlsx, ods, or both.")

        else:
            print("Please enter a value between 1 and 200 MPa.")

    except ValueError:
        print("Invalid input! Please enter a numerical value.")
