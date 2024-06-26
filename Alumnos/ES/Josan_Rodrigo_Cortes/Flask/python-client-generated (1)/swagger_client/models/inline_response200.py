# coding: utf-8

"""
    Api información del sensor de los robots

    Esta API nos proporciona la información almacenada en la base de datos de la empresa Ejemplo de cada uno de sus sensores  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'fechamuestreo': 'str',
        'unidad': 'str',
        'medicion': 'str'
    }

    attribute_map = {
        'code': 'code',
        'fechamuestreo': 'fechamuestreo',
        'unidad': 'unidad',
        'medicion': 'medicion'
    }

    def __init__(self, code=None, fechamuestreo=None, unidad=None, medicion=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._fechamuestreo = None
        self._unidad = None
        self._medicion = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if fechamuestreo is not None:
            self.fechamuestreo = fechamuestreo
        if unidad is not None:
            self.unidad = unidad
        if medicion is not None:
            self.medicion = medicion

    @property
    def code(self):
        """Gets the code of this InlineResponse200.  # noqa: E501

        ID del sensor  # noqa: E501

        :return: The code of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse200.

        ID del sensor  # noqa: E501

        :param code: The code of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def fechamuestreo(self):
        """Gets the fechamuestreo of this InlineResponse200.  # noqa: E501

        Fecha de muestreo  # noqa: E501

        :return: The fechamuestreo of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._fechamuestreo

    @fechamuestreo.setter
    def fechamuestreo(self, fechamuestreo):
        """Sets the fechamuestreo of this InlineResponse200.

        Fecha de muestreo  # noqa: E501

        :param fechamuestreo: The fechamuestreo of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._fechamuestreo = fechamuestreo

    @property
    def unidad(self):
        """Gets the unidad of this InlineResponse200.  # noqa: E501

        Unidad de medida  # noqa: E501

        :return: The unidad of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._unidad

    @unidad.setter
    def unidad(self, unidad):
        """Sets the unidad of this InlineResponse200.

        Unidad de medida  # noqa: E501

        :param unidad: The unidad of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._unidad = unidad

    @property
    def medicion(self):
        """Gets the medicion of this InlineResponse200.  # noqa: E501

        Valor de la medición  # noqa: E501

        :return: The medicion of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._medicion

    @medicion.setter
    def medicion(self, medicion):
        """Sets the medicion of this InlineResponse200.

        Valor de la medición  # noqa: E501

        :param medicion: The medicion of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._medicion = medicion

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
