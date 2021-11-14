from django.test import TestCase

# Create your tests here.
import idanalyzer

try:
    # Initialize Core API with your api key and region (US/EU)
    coreapi = idanalyzer.CoreAPI("A1KZSQjcLv8qoCbSRumHafArTQvEHCQu", "US")

    # Raise exceptions for API level errors
    coreapi.throw_api_exception(True)

    # enable document authentication using quick module
    coreapi.enable_authentication(True, 'quick')
    # coreapi.check_expiry(True)
    # coreapi.enable_aml_check(True)
    # coreapi.generate_contract("Template ID", "PDF")
    coreapi.restrict_type("DI")

    """ Optional settings
    coreapi.enable_vault(True,False,False,False)  # enable vault cloud storage to store document information and image
    coreapi.set_biometric_threshold(0.6) # make face verification more strict
    coreapi.enable_authentication(True, 2) # check if document is real using module v2
    coreapi.enable_barcode_mode(False) # disable OCR and scan for AAMVA barcodes only
    coreapi.enable_image_output(True,True,"url") # output cropped document and face region in URL format
    coreapi.enable_dualside_check(True) # check if data on front and back of ID matches
    coreapi.set_vault_data("user@example.com",12345,"AABBCC") # store custom data into vault
    coreapi.restrict_country("US,CA,AU") # accept documents from United States, Canada and Australia
    coreapi.restrict_state("CA,TX,WA") # accept documents from california, texas and washington
    coreapi.restrict_type("DI") # accept only driver license and identification card
    coreapi.set_ocr_image_resize(0) # disable OCR resizing
    coreapi.verify_expiry(True) # check document expiry
    coreapi.verify_age("18-120") # check if person is above 18
    coreapi.verify_dob("1990/01/01") # check if person's birthday is 1990/01/01
    coreapi.verify_document_number("X1234567") # check if the person's ID number is X1234567
    coreapi.verify_name("Elon Musk") # check if the person is named Elon Musk
    coreapi.verify_address("123 Sunny Rd, California") # check if address on ID matches with provided address
    coreapi.verify_postcode("90001") # check if postcode on ID matches with provided postcode
    coreapi.enable_aml_check(True)  # enable AML/PEP compliance check
    coreapi.set_aml_database("global_politicians,eu_meps,eu_cors")  # limit AML check to only PEPs
    coreapi.enable_aml_strict_match(True)  # make AML matching more strict to prevent false positives
    coreapi.generate_contract("Template ID", "PDF", {"email":"user@example.com"}) # generate a PDF document autofilled with data from user ID
    """

    # perform scan
    response = coreapi.scan(document_primary="/Users/sumitbarua/Documents/CS5820Project/teamocr/appocr/static/images/license_2.jpg")

    # dual-side scan
    # response = coreapi.scan(document_primary="id_front.jpg", document_secondary="id_back.jpg")

    # video biometric verification
    # response = coreapi.scan(document_primary="id_front.jpg", biometric_video="face_video.mp4", biometric_video_passcode="1234")


    # All the information about this ID will be returned in response dictionary
    print(response)

    # Print document holder name
    if response.get('result'):
        data_result = response['result']
        # print("Hello your name is {} {}".format(data_result['firstName'],data_result['lastName']))
        print("Full Name: {} {}\n".format(data_result['firstName'],data_result['lastName']))
        print("DOB: {}\n".format(data_result['dob']))
        print("Address: {} {}\n".format(data_result['address1'], data_result['address2']))
        print("State: {}\n".format(data_result['issuerOrg_region_full']))
        print("LicenseNo: {}\n".format(data_result['documentNumber']))

    
   
    # # Parse document authentication results
    # if response.get('authentication'):
    #     authentication_result = response['authentication']
    #     if authentication_result['score'] > 0.5:
    #         print("The document uploaded is authentic")
    #     elif authentication_result['score'] > 0.3:
    #         print("The document uploaded looks little bit suspicious")
    #     else:
    #         print("The document uploaded is fake")


except idanalyzer.APIError as e:
    # If API returns an error, catch it
    details = e.args[0]
    print("API error code: {}, message: {}".format(details["code"], details["message"]))
except Exception as e:
    print(e)