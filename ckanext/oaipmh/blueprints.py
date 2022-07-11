from flask import Blueprint
from ckan.plugins import toolkit
import logging

import oaipmh.metadata as oaimd
import oaipmh.server as oaisrv
#from pylons import request, response

#from ckan.lib.base import BaseController, render
from ckanext.oaipmh.oaipmh_server import CKANServer
#from rdftools import rdf_reader, dcat2rdf_writer
from ckanext.oaipmh.datacite_writer import datacite_writer
from ckanext.oaipmh.eudatcore_writer import eudatcore_writer

#log = logging.getLogger(__name__)

oai = Blueprint('oai', __name__)

@oai.route('/oai', endpoint='b2find_oai', methods=['POST', 'GET'])

def b2find_oai():
    if 'verb' in toolkit.request.params:
        verb = toolkit.request.params['verb'] if toolkit.request.params['verb'] else None
        if verb:
            client = CKANServer()
            metadata_registry = oaimd.MetadataRegistry()
            metadata_registry.registerReader('oai_dc', oaimd.oai_dc_reader)
            metadata_registry.registerWriter('oai_dc', oaisrv.oai_dc_writer)
            # metadata_registry.registerReader('rdf', rdf_reader)
            # metadata_registry.registerWriter('rdf', dcat2rdf_writer)
            metadata_registry.registerWriter('oai_datacite', datacite_writer)
            metadata_registry.registerWriter('oai_eudatcore', eudatcore_writer)
            serv = oaisrv.BatchingServer(client,
                                         metadata_registry=metadata_registry,
                                         resumption_batch_size=500)
#            parms = toolkit.request.params.mixed()
            parms = toolkit.request.params
            res = serv.handleRequest(parms)
            toolkit.response.headers['content-type'] = 'text/xml; charset=utf-8'
            return res
    return {}
