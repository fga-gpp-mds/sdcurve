from rest_framework import serializers


class PerimeterCurveSerializer(serializers.Serializer):
    """
    Serializer cephalic perimeter curve class.
    """

    title = serializers.CharField(read_only=True)

    ages = serializers.ListField(
        child=serializers.IntegerField(read_only=True)
    )

    percentis_3 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_10 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_25 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_50 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_75 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_90 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_97 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    graphic = serializers.SerializerMethodField()

    def get_graphic(self, obj):
        """
        Get the graphic to plot with google charts
        """

        return self.context['graphic']


class PerimeterCurveResultSerializer(serializers.Serializer):
    """
    serialize the result of the curve query
    """

    perimeter = serializers.FloatField(min_value=0)
    age = serializers.IntegerField(min_value=0)

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = serializers.ChoiceField(choices=GENDERS)
