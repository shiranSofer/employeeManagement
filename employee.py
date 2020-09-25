import json


class Employee:
    """
    Employee.
    """

    def __init__(self, employee_id: int, name: str):
        """
        init employee
        :param employee_id: employee id.
        :param name: name.
        """
        self._employee_id = employee_id
        self._name = name

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def save_employee(self):
        """
        save employee.
        :return:
        """
        try:
            with open("employee.json", "r") as f:
                data = json.load(f)

            temp = data['employee_details']


            # python object to be appended
            employee = {"employee_id": self._employee_id, "employee_name": self._name}

            # appending data to emp_details
            temp.append(employee)
            with open("employee.json", 'w') as f:
                json.dump(data, f)

        except Exception as error:
            print(error)

    def if_exist(self):
        with open("employee.json", "r") as f:
            data = json.load(f)

        temp = data['employee_details']
        print(list(filter(lambda em: em['employee_id'] == str(self._employee_id), temp)))
        return list(filter(lambda em: em['employee_id'] == str(self._employee_id), temp))


    def __str__(self):
        return f"{self._name}, {self._employee_id}"
