from dry_rest_permissions.generics import DRYPermissions


class ServiceDRYPermissions(DRYPermissions):
    """
    Customização para o DRYPermissions utilizar a nossa camada service,
    e não o model!
    """

    def _get_permission_target(self, view, obj=None):
        return view.get_service()
