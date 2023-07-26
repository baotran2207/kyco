def get_new_otp_message(code) -> dict:
    return dict(
        {
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": "<html><body><p>This is your secret login code:</p>"
                    f"<h3>{code}</h3></body></html>",
                },
                "Text": {"Charset": "UTF-8", "Data": f"Your secret login code: {code}"},
            },
            "Subject": {"Charset": "UTF-8", "Data": "Your secret login code"},
        },
    )


def render_porfolio_message(values) -> dict:
    value_in_usd = "${:,.2f}".format(round(values.get("current_amount_in_usd"), 2))
    value_in_vnd = "VND{:,.0f}".format(round(values.get("current_amount_in_vnd"), 0))

    deposit_vnd = "VND{:,.0f}".format(round(values.get("deposits").get("capital_vnd")))
    deposit_usd = "${:,.2f}".format(round(values.get("deposits").get("capital_usd")))

    average_buy_price = "VND{:,.0f}".format(
        round(values.get("deposits").get("average_buy_price"))
    )
    current_usd_price = "VND{:,.2f}".format(round(values.get("current_usd_price")))
    capital_usd_deployed = "${:,.2f}".format(round(values.get("capital_usd_deployed")))
    capital_vnd_deployed = "VND{:,.0f}".format(
        round(values.get("capital_vnd_deployed"))
    )
    stables_amount = "${:,.2f}".format(round(values.get("stables_amount")))
    stables_amount_vnd = "VND{:,.0f}".format(
        round(values.get("stables_amount") * values.get("current_usd_price"))
    )

    link_price = "${}".format(values.get("link_price"))
    link_price_breakevent = "${}".format(values.get("link_price_breakevent"))
    link_position_value = "${:,.2f}".format(round(values.get("link_position_value")))
    link_position_value_vnd = "VND{:,.0f}".format(
        round(values.get("link_position_value") * values.get("current_usd_price"))
    )
    link_position_amount = "{:,}".format(round(values.get("link_position_amount"), 2))

    subject = f"{values.get('PNL').get('position_pnl_usd')}- {link_position_amount} ({link_position_value}) - {link_price}({link_price_breakevent}) "
    return dict(
        {
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": "<html><body><p>Overview:</p>"
                    f"<p>Chainlink          </p>"
                    f"<p>   - Amount          : {link_position_amount} </p>"
                    f"<p>   - Price           : {link_price} - ({link_position_value}) </p>"
                    f"<p>   - average buy at  : {link_price_breakevent} - ({capital_usd_deployed}) </p>"
                    f"<br/>"
                    f"<p>Deposit              </p> "
                    f"<p>- Total deposit      : {deposit_usd} ({deposit_vnd})</p> "
                    f"<p>- Average buy price  : {average_buy_price}</p> "
                    f"<p>- Current price      : {current_usd_price}</p> "
                    f"<p>- Stables amount     : {stables_amount} ({stables_amount_vnd}) </p>"
                    f"<p>- Current values     : {value_in_usd} ({value_in_vnd})</p>"
                    f"<p>- PNL total          : {values.get('PNL').get('pnl_in_usd')} ({values.get('PNL').get('pnl_in_vnd')}) </p>"
                    f"<p>- Current position   : {link_position_value}({link_position_value_vnd})</p>"
                    f"<p>- PNL position       : {values.get('PNL').get('position_pnl_usd')} ({values.get('PNL').get('position_pnl_vnd')}) </p>"
                    f"</body></html>",
                },
                "Text": {"Charset": "UTF-8", "Data": f"{values}"},
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": subject,
            },
        },
    )
