from typing import List
from rest_access_policy import AccessPolicy
from rest_access_policy.access_policy import Statement
from policy.models import PolicyDefinition
import json
import os


class BaseAccessPolicy(AccessPolicy):
    def get_policy_statements(self, request, view) -> List[dict | Statement]:
        try:
            policy = PolicyDefinition.objects.get(slug=self.slug)
            return policy.definition
        except PolicyDefinition.DoesNotExist:
            try:
                curr = os.path.dirname(__file__)
                file_path = os.path.join(curr, f"../policy/policies/{self.slug}.json")
                file_path = os.path.normpath(file_path)
                with open(file_path, "r") as file:
                    data = json.load(file)
                return data
            except FileNotFoundError:
                return []
            except json.JSONDecodeError:
                return []
