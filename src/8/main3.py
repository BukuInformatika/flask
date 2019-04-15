elif request.method == 'DELETE':
        if not len(args) is 0:
            if 'field' in args:
                response = delete_column(response, args['field'])