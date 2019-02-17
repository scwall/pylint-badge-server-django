for report in pylint_generator.get_warning:
    error_pep8 = ConventionPep8.objects.filter(message_id=report['message-id'])
    if not error_pep8:
        error_pep8 = ConventionPep8.objects.create(message=report['message'], symbol=report['symbol'],
                                                   message_id=report['message-id'])

    Reports.objects.create(line=report['line'],
                           path=report['path'],
                           column=report['column'],
                           module=report['module'],
                           obj=report['obj'],
                           pep8=error_pep8,
                           repository=repository
                           )