# -*- coding: utf-8 -*- #
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Revoke credentials being used by Application Default Credentials."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os

from googlecloudsdk.api_lib.auth import util as auth_util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions as c_exc
from googlecloudsdk.core import log
from googlecloudsdk.core.console import console_io
from googlecloudsdk.core.credentials import store as c_store

from oauth2client import client


class Revoke(base.SilentCommand):
  """Revoke previously generated Application Default Credentials.

  Revokes Application Default Credentials that have been previously generated by
  `{parent_command} login` and deletes the local credential file.

  This does not affect any credentials set up through other means,
  such as credentials referenced by the Application Default Credentials
  environment variable or service account credentials that are active on
  a Google Compute Engine virtual machine.
  """

  @staticmethod
  def Args(parser):
    pass

  def Run(self, args):
    """Revoke Application Default Credentials."""

    cred_file = auth_util.ADCFilePath()
    if not os.path.isfile(cred_file):
      raise c_exc.BadFileException(
          'Application Default Credentials have not been set up, nothing was '
          'revoked.')

    creds = client.GoogleCredentials.from_stream(cred_file)
    if creds.serialization_data['type'] != 'authorized_user':
      raise c_exc.BadFileException(
          'The given credential file is a service account credential, and '
          'cannot be revoked.')

    console_io.PromptContinue(
        'You are about to revoke the credentials stored in: [{file}]'
        .format(file=cred_file),
        throw_if_unattended=True, cancel_on_no=True)

    c_store.RevokeCredentials(creds)
    os.remove(cred_file)
    log.status.Print('Credentials revoked.')
