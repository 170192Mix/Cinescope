def log_request_and_response(self, response):
    """
    Логирование запросов и ответов.
    :param response: Объект ответа requests.Response.
    """
    try:
        request = response.request
        GREEN = '\033[32m'
        RED = '\033[31m'
        RESET = '\033[0m'
        headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
        full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

        body = ""
        if hasattr(request, 'body') and request.body is not None:
            if isinstance(request.body, bytes):
                body = request.body.decode('utf-8')
            body = f"-d '{body}' \n" if body != '{}' else ''

        self.logger.info(f"\n{'=' * 40} REQUEST {'=' * 40}")
        self.logger.info(
            f"{GREEN}{full_test_name}{RESET}\n"
            f"curl -X {request.method} '{request.url}' \\\n"
            f"{headers} \\\n"
            f"{body}"
        )

        response_status = response.status_code
        is_success = response.ok
        response_data = response.text

        try:
            response_data = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            pass

        self.logger.info(f"\n{'=' * 40} RESPONSE {'=' * 40}")
        if not is_success:
            self.logger.info(
                f"\tSTATUS_CODE: {RED}{response_status}{RESET}\n"
                f"\tDATA: {RED}{response_data}{RESET}"
            )
        else:
            self.logger.info(
                f"\tSTATUS_CODE: {GREEN}{response_status}{RESET}\n"
                f"\tDATA:\n{response_data}"
            )
        self.logger.info(f"{'=' * 80}\n")
    except Exception as e:
        self.logger.error(f"\nLogging failed: {type(e)} - {e}")
