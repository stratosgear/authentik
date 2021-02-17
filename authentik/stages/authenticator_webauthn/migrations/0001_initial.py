# Generated by Django 3.1.6 on 2021-02-17 10:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentik_flows", "0016_auto_20201202_1307"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebAuthnDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=200)),
                ("credential_id", models.CharField(max_length=300, unique=True)),
                ("public_key", models.TextField()),
                ("sign_count", models.IntegerField(default=0)),
                ("rp_id", models.CharField(max_length=253)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "last_used_on",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuthenticateWebAuthnStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_flows.stage",
                    ),
                ),
                (
                    "configure_flow",
                    models.ForeignKey(
                        blank=True,
                        help_text="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="authentik_flows.flow",
                    ),
                ),
            ],
            options={
                "verbose_name": "WebAuthn Authenticator Setup Stage",
                "verbose_name_plural": "WebAuthn Authenticator Setup Stages",
            },
            bases=("authentik_flows.stage", models.Model),
        ),
    ]
