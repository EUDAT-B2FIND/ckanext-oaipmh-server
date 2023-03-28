# OAI-PMH Extension for CKAN

OAI-PMH API for B2FIND CKAN. 
This extends b2find CKAN to produce OAI-PMH metadata in DataCite format. Ckanext-oaipmh-server is based on https://github.com/kata-csc/ckanext-oaipmh

**Note**: needs hotfix for resumption token & "About" section in pyoai v.2.5.0, see here: https://github.com/infrae/pyoai/pull/53
We extended pyoai by "About" section (provenance info), see here: https://github.com/EUDAT-B2FIND/pyoai/tree/prov_py3

The list of supported verbs consists of:

* GetRecord: fetches a single dataset.
* Identify: Displays information about this OAI-PMH server.
* ListIdentifiers: fetches individual datasets' identifiers.
* ListSets: fetches identifiers of sets.
* ListRecords
* ListMetadataFormats

The usage is documented in: 

https://www.openarchives.org/OAI/openarchivesprotocol.html#ProtocolMessages

## Installation in CKAN
1. Install patched pyoai
```
git clone https://github.com/EUDAT-B2FIND/pyoai.git
cd pyoai
git checkout prov_py3
pip install -e .
```

2. Install extension.
```
git clone https://github.com/EUDAT-B2FIND/ckanext-oaipmh-server.git
cd ckanext-oaipmh-server
pip install -r requirements.txt
pip install -e .
```

3. Configure CKAN
```
vim /etc/ckan-2.9/default/ckan.ini
# add oaiphm extension
ckan.plugins = stats text_view image_view recline_view b2find oaipmh
```

4. Restart CKAN
```
systemctl restart supervisord
```
