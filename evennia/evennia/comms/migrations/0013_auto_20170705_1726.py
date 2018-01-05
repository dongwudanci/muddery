# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 17:26
from __future__ import unicode_literals

from django.db import migrations, models, connection


def _table_exists(db_cursor, tablename):
    "Returns bool if table exists or not"
    return tablename in connection.introspection.table_names()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_copy_player_to_account'),
        ('comms', '0012_merge_20170617_2017'),
    ]

    db_cursor = connection.cursor()

    operations = [
        migrations.AddField(
            model_name='channeldb',
            name='db_account_subscriptions',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='account_subscription_set', to='accounts.AccountDB', verbose_name=b'account subscriptions'),
        ),
        migrations.AlterField(
            model_name='channeldb',
            name='db_object_subscriptions',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='object_subscription_set', to='objects.ObjectDB', verbose_name=b'object subscriptions'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_receivers_scripts',
            field=models.ManyToManyField(blank=True, help_text=b'script_receivers', related_name='receiver_script_set', to='scripts.ScriptDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_sender_scripts',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='sender_script_set', to='scripts.ScriptDB', verbose_name=b'sender(script)'),
        ),
        migrations.AlterField(
            model_name='channeldb',
            name='db_object_subscriptions',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='object_subscription_set', to='objects.ObjectDB', verbose_name=b'object subscriptions'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_receivers_scripts',
            field=models.ManyToManyField(blank=True, help_text=b'script_receivers', related_name='receiver_script_set', to='scripts.ScriptDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_sender_scripts',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='sender_script_set', to='scripts.ScriptDB', verbose_name=b'sender(script)'),
        ),
    ]

    if _table_exists(db_cursor, 'comms_msg_db_hide_from_players'):
        # OBS - this is run BEFORE migrations are run!
        # not a migration of an existing database
        operations += [
            migrations.AddField(
                model_name='channeldb',
                name='db_account_subscriptions',
                field=models.ManyToManyField(blank=True, db_index=True, related_name='account_subscription_set', to='accounts.AccountDB', verbose_name=b'account subscriptions'),
            ),
            migrations.AddField(
                model_name='msg',
                name='db_hide_from_accounts',
                field=models.ManyToManyField(blank=True, related_name='hide_from_accounts_set', to='accounts.AccountDB'),
            ),
            migrations.AddField(
                model_name='msg',
                name='db_receivers_accounts',
                field=models.ManyToManyField(blank=True, help_text=b'account receivers', related_name='receiver_account_set', to='accounts.AccountDB'),
            ),
            migrations.AddField(
                model_name='msg',
                name='db_sender_accounts',
                field=models.ManyToManyField(blank=True, db_index=True, related_name='sender_account_set', to='accounts.AccountDB', verbose_name=b'sender(account)'),
            ),
        ]
