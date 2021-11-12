OAI-PMH API for B2FIND CKAN. 
This extends b2find CKAN to produce OAI-PMH metadata in DataCite format. Ckanext-oaipmh-server is based on https://github.com/kata-csc/ckanext-oaipmh

**Note**: needs hotfix for resumption token in pyoai v.2.5.0, see here: https://github.com/EUDAT-B2FIND/pyoai/blob/03c790431d96024b29f3cd8575602d996350ff80/src/oaipmh/server.py#L458

The list of supported verbs consists of:

* GetRecord: fetches a single dataset.
* Identify: Displays information about this OAI-PMH server.
* ListIdentifiers: fetches individual datasets' identifiers.
* ListSets: fetches identifiers of sets.
* ListRecords
* ListMetadataFormats

The usage is documented in: 

https://www.openarchives.org/OAI/openarchivesprotocol.html#ProtocolMessages
