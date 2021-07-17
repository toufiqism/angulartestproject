package com.sample.foo.simplewidget;

import android.annotation.SuppressLint;
import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.util.Log;
import android.widget.RemoteViews;

import java.util.Random;

import static androidx.core.content.ContextCompat.startActivity;

public class SimpleWidgetProvider extends AppWidgetProvider {

    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        final int count = appWidgetIds.length;


        for (int i = 0; i < count; i++) {
            int widgetId = appWidgetIds[i];
            @SuppressLint("DefaultLocale")
            String number = String.format("%03d", (new Random().nextInt(900) + 100));

            RemoteViews remoteViews = new RemoteViews(context.getPackageName(),
                    R.layout.simple_widget);
            remoteViews.setTextViewText(R.id.textView, number);

            Intent intent = new Intent(context, SimpleWidgetProvider.class);

            intent.setAction(AppWidgetManager.ACTION_APPWIDGET_UPDATE);
            intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_IDS, appWidgetIds);
            PendingIntent pendingIntent = PendingIntent.getBroadcast(context,
                    0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
            remoteViews.setOnClickPendingIntent(R.id.actionButton, pendingIntent);

            Intent cIntent = new Intent(Intent.ACTION_CALL);
            cIntent.setData(Uri.parse("tel:" + "*566#"));
//            context.startActivity(cIntent);

            PendingIntent pendingIntent2 = PendingIntent.getBroadcast(context,
                    0, cIntent, PendingIntent.FLAG_UPDATE_CURRENT);
            remoteViews.setOnClickPendingIntent(R.id.actionButton, pendingIntent2);

            appWidgetManager.updateAppWidget(widgetId, remoteViews);
        }
    }
}
