import saml2
from saml2.saml import NAME_FORMAT_URI

BASE = "https://{{matrix_domain}}:8443/"

CONFIG = {
    "entityid": "matrix",
    "description": "Matrix Server",
    "service": {
        "sp": {
            "name": "matrix-login",
            "endpoints": {
                "single_sign_on_service": [
                    (BASE + "_matrix/saml2/authn_response", saml2.BINDING_HTTP_POST),
                ],
                "assertion_consumer_service": [
                    (BASE + "_matrix/saml2/authn_response", saml2.BINDING_HTTP_POST),
                ],
                #"single_logout_service": [
                #    (BASE + "_matrix/saml2/logout", saml2.BINDING_HTTP_POST),
                #],
            },
            "required_attributes": ["uid",],
            "optional_attributes": ["displayName"],
            "sign_assertion": True,
            "sign_response": True,
        }
    },
    "debug": 0,
    "key_file": "/data/saml/key.pem",
    "cert_file": "/data/saml/cert.pem",
    "encryption_keypairs": [
        {
            "key_file": "/data/saml/key.pem",
            "cert_file": "/data/saml/cert.pem",
        }
    ],
    "attribute_map_dir": "/data/saml/saml2_attribute_maps/",
    "metadata": {
        "local": ["/data/saml/idp.xml"]
    },
    # If you want to have organization and contact_person for the pysaml2 config
    #"organization": {
    #    "name": "Example AB",
    #    "display_name": [("Example AB", "se"), ("Example Co.", "en")],
    #    "url": "http://example.com/roland",
    #},
    #"contact_person": [{
    #    "given_name": "Example",
    #    "sur_name": "Example",
    #    "email_address": ["example@example.com"],
    #    "contact_type": "technical",
    #    },
    #],
    # Make sure to have xmlsec1 installed on your host(s)!
    "xmlsec_binary": "/usr/bin/xmlsec1",
    "name_form": NAME_FORMAT_URI,
}
