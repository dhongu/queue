# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    # Databases already on the dhongu/queue 20.0 fork (20.0.2.0.x, before the
    # alignment with OCA/queue 20.0) skip the 19.0.2.2.0 step: drop the old
    # autovacuum cron here too, its model.autovacuum() method is gone.
    openupgrade.delete_records_safely_by_xml_id(
        env,
        ["queue_job.ir_cron_autovacuum_queue_jobs"],
    )
