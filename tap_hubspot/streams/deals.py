from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class DealsStream(HubSpotStream):
    """Deals."""

    name = "deals"
    search_path = "/crm/v3/objects/deals/search"
    full_path = "/crm/v3/objects/deals"
    properties_object_type = "deals"
    primary_keys = ["id"]

    @property
    def schema(self):
        props = th.PropertiesList(
            th.Property(
                "id",
                th.StringType,
            ),
            th.Property(
                "properties",
                th.StringType,
            ),
            th.Property(
                "createdAt",
                th.DateTimeType,
            ),
            th.Property(
                "updatedAt",
                th.DateTimeType,
            ),
            th.Property(
                "archived",
                th.BooleanType,
            ),
            th.Property(
                "archivedAt",
                th.DateTimeType,
            ),
            th.Property(
                "associations",
                th.StringType,
            ),
        )

        # Needs to be defined manually since 2024-01-02 when
        # the list of properties in hubspot became to long for a request.
        # Error: 414 Client Error: URI Too Long for path
        self.extra_properties = [
            "abrs_signed",
            "amount_in_home_currency",
            "background_check_complete",
            "connected_with_carrier_",
            "days_to_close",
            "deal_currency_code",
            "deal_source",
            "did_you_slack_csm_in_sales_force_to_send_dcaa_",
            "dq_file_sent",
            "driver_marked_as_hired_in_foley",
            "driver_passed_orientation",
            "driver_qualified_for_company",
            "full_profile_status",
            "has_the_driver_been_applied_to_the_carrier_",
            "hs_acv",
            "hs_all_assigned_business_unit_ids",
            "hs_all_collaborator_owner_ids",
            "hs_all_deal_split_owner_ids",
            "hs_analytics_latest_source",
            "hs_analytics_latest_source_company",
            "hs_analytics_latest_source_contact",
            "hs_analytics_latest_source_data_1",
            "hs_analytics_latest_source_data_1_company",
            "hs_analytics_latest_source_data_1_contact",
            "hs_analytics_latest_source_data_2",
            "hs_analytics_latest_source_data_2_company",
            "hs_analytics_latest_source_data_2_contact",
            "hs_analytics_latest_source_timestamp",
            "hs_analytics_latest_source_timestamp_company",
            "hs_analytics_latest_source_timestamp_contact",
            "hs_analytics_source",
            "hs_analytics_source_data_1",
            "hs_analytics_source_data_2",
            "hs_arr",
            "hs_campaign",
            "hs_closed_amount",
            "hs_closed_amount_in_home_currency",
            "hs_closed_won_count",
            "hs_closed_won_date",
            "hs_created_by_user_id",
            "hs_days_to_close_raw",
            "hs_deal_amount_calculation_preference",
            "hs_deal_score",
            "hs_deal_stage_probability",
            "hs_deal_stage_probability_shadow",
            "hs_exchange_rate",
            "hs_forecast_amount",
            "hs_forecast_probability",
            "hs_is_closed",
            "hs_is_closed_won",
            "hs_is_deal_split",
            "hs_is_open_count",
            "hs_lastmodifieddate",
            "hs_likelihood_to_close",
            "hs_line_item_global_term_hs_discount_percentage",
            "hs_line_item_global_term_hs_discount_percentage_enabled",
            "hs_line_item_global_term_hs_recurring_billing_period",
            "hs_line_item_global_term_hs_recurring_billing_period_enabled",
            "hs_line_item_global_term_hs_recurring_billing_start_date",
            "hs_line_item_global_term_hs_recurring_billing_start_date_enabled",
            "hs_line_item_global_term_recurringbillingfrequency",
            "hs_line_item_global_term_recurringbillingfrequency_enabled",
            "hs_manual_forecast_category",
            "hs_merged_object_ids",
            "hs_mrr",
            "hs_next_step",
            "hs_num_associated_active_deal_registrations",
            "hs_num_associated_deal_registrations",
            "hs_num_associated_deal_splits",
            "hs_num_of_associated_line_items",
            "hs_num_target_accounts",
            "hs_object_id",
            "hs_object_source",
            "hs_object_source_id",
            "hs_object_source_label",
            "hs_object_source_user_id",
            "hs_pinned_engagement_id",
            "hs_predicted_amount",
            "hs_predicted_amount_in_home_currency",
            "hs_priority",
            "hs_projected_amount",
            "hs_projected_amount_in_home_currency",
            "hs_read_only",
            "hs_source_object_id",
            "hs_tag_ids",
            "hs_tcv",
            "hs_unique_creation_key",
            "hs_updated_by_user_id",
            "hs_user_ids_of_all_notification_followers",
            "hs_user_ids_of_all_notification_unfollowers",
            "hs_user_ids_of_all_owners",
            "hs_was_imported",
            "hubspot_owner_assigneddate",
            "is_the_driver_a_lf_driver_",
            "job_class",
            "lanefinder_profile_status",
            "lead_source",
            "lf_priority",
            "lws_link_signed",
            "manual_deal_source",
            "msa_date_sent",
            "msa_status",
            "mvr_passed_",
            "mvr_passed__date_",
            "nass_sent",
            "number_of_tractors__cloned_",
            "onboarded_to_people_lease",
            "power_apply_candidate_name",
            "power_apply_carrier_email",
            "power_apply_carrier_number",
            "power_apply_recipient_email",
            "request_created_by",
            "request_happend_at",
            "requested_time_to_contact",
            "sales_manager",
            "start_date_set",
            "test",
            "test3",
            "tractor_trailer_experience",
            "dealname",
            "recurring_revenue_amount",
            "recurring_revenue_inactive_date",
            "amount",
            "recurring_revenue_deal_type",
            "recurring_revenue_inactive_reason",
            "dealstage",
            "pipeline",
            "closedate",
            "createdate",
            "engagements_last_meeting_booked",
            "engagements_last_meeting_booked_campaign",
            "engagements_last_meeting_booked_medium",
            "engagements_last_meeting_booked_source",
            "hs_latest_meeting_activity",
            "hs_sales_email_last_replied",
            "hubspot_owner_id",
            "notes_last_contacted",
            "notes_last_updated",
            "notes_next_activity_date",
            "num_contacted_notes",
            "num_notes",
            "hs_createdate",
            "hubspot_team_id",
            "dealtype",
            "hs_all_owner_ids",
            "description",
            "hs_all_team_ids",
            "hs_all_accessible_team_ids",
            "num_associated_contacts",
            "closed_lost_reason",
            "closed_won_reason"
        ]

        if self.replication_key:
            props.append(
                th.Property(
                    self.replication_key,
                    th.DateTimeType,
                )
            )

        return props.to_dict()

    @property
    def replication_key(self) -> Optional[str]:
        return None if self.config.get("no_search", False) else "hs_lastmodifieddate"

    @replication_key.setter
    def replication_key(self, _):
        "Just to shut Lint up"
        pass

    @property
    def path(self) -> str:
        return (
            self.full_path if self.config.get("no_search", False) else self.search_path
        )

    @path.setter
    def path(self, _):
        "Just to shut Lint up"
        pass
