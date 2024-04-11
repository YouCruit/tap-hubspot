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
            "hs_campaign",
            "hs_closed_amount",
            "hs_closed_amount_in_home_currency",
            "hs_closed_won_count",
            "hs_closed_won_date",
            "hs_created_by_user_id",
            "hs_date_entered_123130520",
            "hs_date_entered_124092432",
            "hs_date_entered_27073029",
            "hs_date_entered_27073031",
            "hs_date_entered_27175459",
            "hs_date_entered_32801071",
            "hs_date_entered_32880394",
            "hs_date_entered_33541463",
            "hs_date_entered_33541464",
            "hs_date_entered_33541465",
            "hs_date_entered_33541466",
            "hs_date_entered_33541467",
            "hs_date_entered_33541469",
            "hs_date_entered_33559723",
            "hs_date_entered_33571088",
            "hs_date_entered_45507610",
            "hs_date_entered_45507611",
            "hs_date_entered_45507612",
            "hs_date_entered_45507613",
            "hs_date_entered_45507614",
            "hs_date_entered_45507615",
            "hs_date_entered_45507616",
            "hs_date_entered_51175044",
            "hs_date_entered_57507971",
            "hs_date_entered_58770509",
            "hs_date_entered_58770510",
            "hs_date_entered_58770511",
            "hs_date_entered_58770512",
            "hs_date_entered_58770513",
            "hs_date_entered_58770514",
            "hs_date_entered_58770515",
            "hs_date_entered_62911107",
            "hs_date_entered_62911108",
            "hs_date_entered_62911109",
            "hs_date_entered_62911110",
            "hs_date_entered_62911111",
            "hs_date_entered_62911112",
            "hs_date_entered_appointmentscheduled",
            "hs_date_entered_closedlost",
            "hs_date_entered_closedwon",
            "hs_date_entered_contractsent",
            "hs_date_entered_decisionmakerboughtin",
            "hs_date_entered_presentationscheduled",
            "hs_date_entered_qualifiedtobuy",
            "hs_date_exited_123130520",
            "hs_date_exited_124092432",
            "hs_date_exited_27073029",
            "hs_date_exited_27073031",
            "hs_date_exited_27175459",
            "hs_date_exited_32801071",
            "hs_date_exited_32880394",
            "hs_date_exited_33541463",
            "hs_date_exited_33541464",
            "hs_date_exited_33541465",
            "hs_date_exited_33541466",
            "hs_date_exited_33541467",
            "hs_date_exited_33541469",
            "hs_date_exited_33559723",
            "hs_date_exited_33571088",
            "hs_date_exited_45507610",
            "hs_date_exited_45507611",
            "hs_date_exited_45507612",
            "hs_date_exited_45507613",
            "hs_date_exited_45507614",
            "hs_date_exited_45507615",
            "hs_date_exited_45507616",
            "hs_date_exited_51175044",
            "hs_date_exited_57507971",
            "hs_date_exited_58770509",
            "hs_date_exited_58770510",
            "hs_date_exited_58770511",
            "hs_date_exited_58770512",
            "hs_date_exited_58770513",
            "hs_date_exited_58770514",
            "hs_date_exited_58770515",
            "hs_date_exited_62911107",
            "hs_date_exited_62911108",
            "hs_date_exited_62911109",
            "hs_date_exited_62911110",
            "hs_date_exited_62911111",
            "hs_date_exited_62911112",
            "hs_date_exited_appointmentscheduled",
            "hs_date_exited_closedlost",
            "hs_date_exited_closedwon",
            "hs_date_exited_contractsent",
            "hs_date_exited_decisionmakerboughtin",
            "hs_date_exited_presentationscheduled",
            "hs_date_exited_qualifiedtobuy",
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
            "hs_manual_forecast_category",
            "hs_merged_object_ids",
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
            "closed_won_reason",
            "complete_reason",
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
