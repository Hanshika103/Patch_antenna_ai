import plotly.graph_objects as go


def create_antenna_3d(
    patch_width,
    patch_length,
    ground_width,
    ground_length,
    substrate_height=1.6,
):
    fig = go.Figure()

    # -----------------------------
    # Ground Plane
    # -----------------------------
    fig.add_trace(
        go.Mesh3d(
            x=[0, ground_width, ground_width, 0],
            y=[0, 0, ground_length, ground_length],
            z=[0, 0, 0, 0],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color="gray",
            opacity=1,
            name="Ground Plane",
        )
    )

    # -----------------------------
    # Substrate
    # -----------------------------
    fig.add_trace(
        go.Mesh3d(
            x=[0, ground_width, ground_width, 0],
            y=[0, 0, ground_length, ground_length],
            z=[
                substrate_height,
                substrate_height,
                substrate_height,
                substrate_height,
            ],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color="green",
            opacity=0.35,
            name="Substrate",
        )
    )

    # -----------------------------
    # Patch
    # -----------------------------
    x0 = (ground_width - patch_width) / 2
    y0 = (ground_length - patch_length) / 2

    fig.add_trace(
        go.Mesh3d(
            x=[
                x0,
                x0 + patch_width,
                x0 + patch_width,
                x0,
            ],
            y=[
                y0,
                y0,
                y0 + patch_length,
                y0 + patch_length,
            ],
            z=[
                substrate_height + 0.05,
                substrate_height + 0.05,
                substrate_height + 0.05,
                substrate_height + 0.05,
            ],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color="gold",
            opacity=1,
            name="Patch",
        )
    )

    # -----------------------------
    # Feed Line
    # -----------------------------
    feed_width = patch_width * 0.08

    fig.add_trace(
        go.Mesh3d(
            x=[
                ground_width / 2 - feed_width / 2,
                ground_width / 2 + feed_width / 2,
                ground_width / 2 + feed_width / 2,
                ground_width / 2 - feed_width / 2,
            ],
            y=[
                0,
                0,
                y0,
                y0,
            ],
            z=[
                substrate_height + 0.05,
                substrate_height + 0.05,
                substrate_height + 0.05,
                substrate_height + 0.05,
            ],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color="orange",
            opacity=1,
            name="Feed Line",
        )
    )

    fig.update_layout(
        title="3D Patch Antenna",
        scene=dict(
            xaxis_title="Width (mm)",
            yaxis_title="Length (mm)",
            zaxis_title="Height (mm)",
            aspectmode="data",
        ),
        height=650,
        margin=dict(l=0, r=0, t=50, b=0),
    )

    return fig

    