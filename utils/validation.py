def validate_order_totals(df):
    df["ChannelSum"] = (
        df["InStoreOrders"] +
        df["UberEatsOrders"] +
        df["DoorDashOrders"] +
        df["SelfDeliveryOrders"]
    )

    df["OrderMismatch"] = df["ChannelSum"] - df["MonthlyOrders"]
    return df

def validate_channel_share(df):
    df["ShareSum"] = (
        df["InStoreShare"] +
        df["UE_share"] +
        df["DD_share"] +
        df["SD_share"]
    )
    return df
