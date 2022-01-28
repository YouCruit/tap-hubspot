# tap-hubspot

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

## Fork details

This fork was created because the official tap hasn't been updated in a good while. Additional features has been added, for example 

- support for [Tickets](https://legacydocs.hubspot.com/docs/methods/tickets/tickets-overview)
- the schema for custom properties has been flattened. Before you'd have a schema such as 'foo: { value: 'bar', updated: '...', updatedBy: '...' } and that was just bloat. This tap instead produces this schema for custom properties: `foo: 'bar'
- requirement for an oauth token has been removed - you should use a hubspot api key to access the api

## Description

This tap:
- Pulls raw data from HubSpot's [REST API](http://developers.hubspot.com/docs/overview)
- Extracts the following resources from HubSpot
  - [Campaigns](http://legacydocs.hubspot.com/docs/methods/email/get_campaign_data)
  - [Companies](http://legacydocs.hubspot.com/docs/methods/companies/get_company)
  - [Contacts](https://legacydocs.hubspot.com/docs/methods/contacts/get_contacts)
  - [Contact Lists](http://legacydocs.hubspot.com/docs/methods/lists/get_lists)
  - [Deals](http://legacydocs.hubspot.com/docs/methods/deals/get_deals_modified)
  - [Deal Pipelines](https://legacydocs.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines)
  - [Email Events](http://legacydocs.hubspot.com/docs/methods/email/get_events)
  - [Engagements](https://legacydocs.hubspot.com/docs/methods/engagements/get-all-engagements)
  - [Forms](http://legacydocs.hubspot.com/docs/methods/forms/v2/get_forms)
  - [Keywords](http://legacydocs.hubspot.com/docs/methods/keywords/get_keywords)
  - [Owners](http://legacydocs.hubspot.com/docs/methods/owners/get_owners)
  - [Subscription Changes](http://legacydocs.hubspot.com/docs/methods/email/get_subscriptions_timeline)
  - [Tickets](https://legacydocs.hubspot.com/docs/methods/tickets/tickets-overview)
  - [Workflows](http://legacydocs.hubspot.com/docs/methods/workflows/v3/get_workflows)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## Configuration

This tap requires a `config.json` which specifies a Hubspot API key and a cutoff date for syncing historical data. See [config.sample.json](config.sample.json) for an example.

To run `tap-hubspot` with the configuration file, use this command:

```bash
› tap-hubspot -c my-config.json
```

---

Copyright &copy; 2017 Stitch
