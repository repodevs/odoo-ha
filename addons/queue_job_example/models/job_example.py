import logging
from time import sleep
from odoo import models

_logger = logging.getLogger(__name__)


class JobExample(models.AbstractModel):
    _name = 'job.example'
    _description = 'Queue Job Example'
   
    def action_do(self):
        _logger.info('action_do start')
        self.with_delay(eta=2).run_in_background()
        _logger.info('action_do done')
        return True

    def run_in_background(self):
        _logger.info(f"Simulating heavy computation, sleep for 3 seconds")
        sleep(3)
        _logger.info('Simulating done')
 