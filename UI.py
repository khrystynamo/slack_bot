#UI
#Button to Confirm Sending Thanks

blocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You are about to send thanks to <@colleague_tag>."
        },
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Details:* Thank you for your hard work on the project!"
            },
            {
                "type": "mrkdwn",
                "text": "*Points:* 50"
            }
        ]
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Confirm"
                },
                "style": "primary",
                "value": "confirm_thanks",
                "action_id": "confirm_thanks_action"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Cancel"
                },
                "style": "danger",
                "value": "cancel_thanks",
                "action_id": "cancel_thanks_action"
            }
        ]
    }
]

#Button for Selecting the Most Appreciated Colleague

blocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "The following colleague has received the most points this month: <@top_colleague_tag>."
        }
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Select for Reward"
                },
                "style": "primary",
                "value": "select_reward",
                "action_id": "select_reward_action"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "View More Details"
                },
                "value": "view_details",
                "action_id": "view_details_action"
            }
        ]
    }
]

 #Button for HR to View Monthly Summary

blocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "HR Summary for this Month"
        }
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "View Summary"
                },
                "style": "primary",
                "value": "view_summary",
                "action_id": "view_summary_action"
            }
        ]
    }
]

blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": 'message'
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Get Another Message"
                    },
                    "action_id": "get_another_message",
                    "value": "get_another_message"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Give Feedback"
                    },
                    "action_id": "give_feedback",
                    "value": "give_feedback"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Share with a Colleague"
                    },
                    "action_id": "share_with_colleague",
                    "value": "share_with_colleague"
                }
            ]
        }
    ]




{
    "display_information": {
        "name": "Thankify"
    },
    "features": {
        "app_home": {
            "home_tab_enabled": True,
            "messages_tab_enabled": False,
            "messages_tab_read_only_enabled": False
        },
        "bot_user": {
            "display_name": "Thankify",
            "always_online": False
        },
        "slash_commands": [
            {
                "command": "/thank_user",
                "url": "https://slack.com/thank_user",
                "description": "If you want to thank your colleague for the precious job they're doing, you can use it to give kudos or even gifts!",
                "should_escape": False
            },
            {
                "command": "/get_support",
                "url": "https://slack.com/get_support",
                "description": "When you want to get an emotional support!",
                "should_escape": False
            },
            {
                "command": "/charity",
                "url": "https://slack.com/charity",
                "description": "Active charity links are here!",
                "should_escape": False
            }
        ]
    },
    "oauth_config": {
        "scopes": {
            "bot": [
                "commands",
                "incoming-webhook",
                "app_mentions:read",
                "channels:history",
                "im:history",
                "users:read",
                "chat:write"
            ]
        }
    },
    "settings": {
        "org_deploy_enabled": False,
        "socket_mode_enabled": False,
        "token_rotation_enabled": False
    }
}